// const url = "{% url 'booking_form' %}";
let unavailable_dates = [];
let slots_taken = {};
const tomorrow = new Date();
tomorrow.setDate(tomorrow.getDate() + 1);
// if tomorrow is Sunday or Monday, move along until the first workday
while ([0, 1].includes(tomorrow.getDay())) {
    tomorrow.setDate(tomorrow.getDate() + 1);
}

// given a length-type of booking update the time picker to the base slots available
function reset_time_picker(length, showTimepicker = true, taken_slots = null) {
    console.log(taken_slots);
    // remove selected value from timepicker and BookingForm time field
    $('#timepicker').val('');
    $('#id_time').val('');
    
    // remove hidden from all time picker options, show or hide timepicker as directed
    $('#timepicker option').removeClass('d-none');
    $('div:has(> #timepicker)').toggleClass('d-none', !showTimepicker);
    // debugger
    const long_slots = ["8:30", "11:00", "13:30", "16:00"];
    const short_slots = ["9:00", "10:00", "11:00", "12:00", "14:00", "15:00", "16:00"];

    // create the array of available slots
    let available_slots = [...(length == 'long' ? long_slots : short_slots)];
    if (taken_slots) {
        available_slots = available_slots.filter((v) => { return !taken_slots.includes(v) })
    }

    // iterate through the slots and hide any that are unavailable for this type or are taken
    $('#timepicker option').each((i, el) => {
        if (!available_slots.includes(el.textContent)) {
            $(el).addClass('d-none');
        }
    });
}

// when document loads
$(function() {
    // set up the datepicker
    $('#datepicker').datepicker({
        dateFormat: 'yy-mm-dd',
        minDate: tomorrow,
        beforeShowDay: function(date) {
            if ([0, 1].includes(date.getDay())) { return [false] }
            let string = jQuery.datepicker.formatDate('yy-mm-dd', date);
            return [unavailable_dates.indexOf(string) == -1]
        },
        // date selector event listener
        onSelect: function(dateText) {
            console.log(dateText);
            let serviceLength = $('.service-selector.selected').data('serviceLength');
            // refresh the timepicker, show it and update the available slots
            reset_time_picker(serviceLength, true, slots_taken[dateText]);
            $('#dt-form-row')[0].scrollIntoView({behavior: "smooth"});
            // set date field in BookingForm and hide dog info and submit
            $('#id_date').val(dateText);
            $('#dog-info-form-row').addClass('d-none');
            $('#booking-form-row').addClass('d-none');
        },
    });

    // retrieve CSRF token to sign the AJAX request
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            const cookies = document.cookie.split(";");
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + "=")) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
    // service selector event listener
    $('#service-form .service-selector').on('click', (e) => {
        // only if not the currently selected service
        if (!$(e.currentTarget).hasClass('selected')) {
            // store the previous service length
            let previousLength = $('.service-selector.selected').data('serviceLength') ?? '';
            
            // remove selected class from all services and add to target
            $('#service-form .service-selector').removeClass('selected');
            $(e.currentTarget).addClass('selected');
            let selected_service_value = $(e.currentTarget).attr('data-service-value');

            // update the field in the booking_form
            $('#id_service > option').attr('selected', false);
            $(`#id_service > option[value=${selected_service_value}]`).attr('selected', true);
            
            // get the service length data and prepare formData for AJAX call
            const formData = {
                slot: $(e.currentTarget).data('serviceLength'),
            }
            // get the url to hit for this AJAX call
            const url = $('#service-form').attr('action');
            
            // AJAX
            $.ajax({
                url: url,
                type: "POST",
                dataType: "json",
                data: JSON.stringify({payload: formData,}),
                headers: {
                    "X-Requested-With": "XMLHttpRequest",
                    "X-CSRFToken": getCookie("csrftoken"),
                },
                success: (data) => {
                    // pump returned data into the availability data variables
                    console.log(data);
                    unavailable_dates = data['unavailable_days'];
                    slots_taken = data['used_slots'];
                },
                error: (error) => {
                    console.log(error);
                }
            });

            // clear the date and time pickers
            $('#datepicker').datepicker('setDate', null);
            $('#timepicker').val("");

            // clear the BookingForm values for date and time
            $('#id_date').val('');
            $('#id_time').val('');

            // show the date/time form, but hide the timepicker, dog info form and submit
            $('#dt-form-row').removeClass('d-none');
            $('div:has(> #timepicker)').addClass('d-none');
            $('#dog-info-form-row').addClass('d-none');
            $('#booking-form-row').addClass('d-none');
            
            // refresh the datepicker, open it and scroll into view
            $('#datepicker').datepicker('refresh');
            $('#dt-form-row')[0].scrollIntoView({behavior: "smooth"});
        }
    });

    // time selector event listener
    $('#timepicker').on('change', (e) => {
        // update BookingForm
        $('#id_time').val($(e.currentTarget).val());
        // reveal the dog information section and scroll it into view
        $('#dog-info-form-row').toggleClass('d-none', $(e.currentTarget).val() == "");
        $('#dog-info-form-row')[0].scrollIntoView({behavior: "smooth"});
        // reveal the submit button
        $('#booking-form-row').toggleClass('d-none', $(e.currentTarget).val() == "");
    });

    // dog info event listeners
    for (let el of ['dog-name', 'dog-breed', 'dog-size', 'dog-additional-notes']) {
        $(`#${el}`).on('change', (e) => {
            let booking_form_id = $(e.currentTarget).attr('data-booking-form-id');
            $(`#${booking_form_id}`).val($(e.currentTarget).val());
        });
    }
});
