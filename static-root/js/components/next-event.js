"use strict";
(function($){
    $.get('/events/json_events_all', function(events){
        // "date < date2" = date1 comes BEFORE date2
        var first_event = getFirstEvent(events);    
        fill_div(first_event);
    });

    function getFirstEvent(events){
        // the Event model orders them by time_start
        var now = new Date(),
            firstEventStartTime = new Date(events[0].fields.time_start);  
        if (now < firstEventStartTime){
            return events[0];
        }
        events.forEach(function(event){
            var eventStart = new Date(event.time_start);
            if (now > event){
                return event;
            }
        });
    }
    function fill_div(event){
        var $name = $('.next-event-name'),
            $location = $('.next-event-location'),
            $time = $('.next-event-time');
        console.log(event);
        $name.html("<a href='/events/" + event.pk + "'>" + event.fields.name + "</a>");
        $time.html(event.fields.time_start);
        $location.html(event.fields.location);
    } 
}(jQuery));