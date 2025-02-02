// Initialize and add the map
let map;

async function initMap() {
  // The location of Uluru
  const position = {
    lat: 55.970975288091324,
    lng: -3.208456,
  };
  // Request needed libraries.
  //@ts-ignore
  const { Map } = await google.maps.importLibrary("maps");
  const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

  // The map, centered at Uluru
  map = new Map(document.getElementById("map"), {
    zoom: 16,
    center: position,
    mapId: "DEMO_MAP_ID",
  });

  // The marker, positioned at Uluru
  const marker = new AdvancedMarkerElement({
    map: map,
    position: position,
    title: "Perfect Paws",
    gmpClickable: true,
  });
}

initMap();
