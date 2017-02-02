var apiKey = 'AIzaSyC75rnKyEkGxmVyG7hlqFicwPBgDmQLN_w';
var calendarId = '2ul10sd9g30mnk1vpmcnnp5qv4@group.calendar.google.com';
var maxResults = 4;

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
}).done(function(data) {

    var $eventsContainer = $('#3 > .row');

    data.items.forEach(function (item) {

        var eventObject = parseDesc(item.description);
        var eventEl = document.createElement('div');
        eventEl.className = 'event';
        eventEl.append(eventObject.venue);
        eventEl.append(document.createElement('hr'));
        $eventsContainer.append(eventEl);
    })

}).fail(function(jqXHR, textStatus, errorThrown) {
    console.log('err')
});

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
