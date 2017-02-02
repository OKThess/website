var apiKey = 'AIzaSyC75rnKyEkGxmVyG7hlqFicwPBgDmQLN_w';
var calendarId = '2ul10sd9g30mnk1vpmcnnp5qv4@group.calendar.google.com';
var maxResults = 4;

var $eventsContainer = $('#3 > .row.events');
var $noEventsEl = $('#3 > .row.no-events')[0];

var calendarUrl = 'https://www.googleapis.com/calendar/v3/calendars/';
calendarUrl += calendarId + '/events?key=';
calendarUrl += apiKey;

var dt = new Date();
calendarUrl += '&orderBy=startTime';
calendarUrl += '&singleEvents=true';
calendarUrl += '&timeMin=' + dt.toISOString();
calendarUrl += '&maxResults=' + maxResults;

$.ajax({
    type: 'GET',
    url: calendarUrl,
    crossDomain: true,
    dataType: 'json'
})
.done(function (data) {
    return renderEvents(data);
})
.fail(function(jqXHR, textStatus, errorThrown) {
    console.log('err')
});

var renderEvents = function (gCalenderApiResponse) {

    var eventsList = gCalenderApiResponse.items.map(constructEventElement);

    if (eventsList.length) {
        $eventsContainer.append(eventsList);
    } else {
        $noEventsEl.style.display = 'block';
    }
}

var constructEventElement = function (event) {
    var extendedInfo = parseDesc(event.description);

    var eventEl = document.createElement('div');
    eventEl.className = 'event';

    var eventName = createElement('div', 'eventName', event.summary);

    var eventDesc = createElement('div', 'eventDesc', extendedInfo.about);

    var eventDate = createElement('div', 'eventDate', new Date(event.start.dateTime).toLocaleDateString());

    eventEl.append(eventName);
    eventEl.append(eventDesc);
    eventEl.append(eventDate);
    eventEl.append(document.createElement('hr'));

    return eventEl;
}

var createElement = function (el, className, content) {

    var element = document.createElement(el);
    element.className = className;

    if (content) {
        element.append(content);
    }

    return element;
}

var parseDesc = function(descr) {

  var out = {
    venue: null,
    infoUrl: null,
    mapUrl: null,
    about: null,
    image: null,
    language: null,
    rest: ''
  };

  if (!descr) {
    return out;
  }

  var lines = descr.split('\n');

  lines.forEach(function(line) {
    if (!line.length) {
      return;
    }

    var splitPos = line.indexOf(':');
    if (splitPos === -1) {
      return;
    }

    var key = line.substr(0, splitPos).toLowerCase().trim();
    var value = line.substr(splitPos + 1).trim();

    switch(key) {
    case 'venue':
      out.venue = value;
      break;
    case 'info':
      out.infoUrl = value;
      break;
    case 'map':
      out.mapUrl = value;
      break;
    case 'about':
      out.about = value;
      break;
    case 'language':
      out.language = value;
      break;
    case 'image':
     out.image = value;
     break;
    default:
      out.rest += line + '<br />';
      break;
    }
  }, this);

  return out;

};
