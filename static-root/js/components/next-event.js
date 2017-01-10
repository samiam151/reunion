"use strict";
(function($){
    $.get('/events/json_events_all', function(events){
        populate_div(getNextEvent(events));
    });

    function getNextEvent(events){
        // the Event model orders events by time_start on export
        // "date < date2" = date1 comes BEFORE date2
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

    function populate_div(event){
        var $name = $('.next-event-name'),
            $location = $('.next-event-location'),
            $time = $('.next-event-time'),
            $date = $('.next-event-date');
        
        var time = new Date(event.fields.time_start),
            event_date = time.toDateString(),
            event_time = to12Hour(time.toTimeString().split(" ")[0]);
        
        $name.html("<a href='/events/" + event.pk + "'>" + event.fields.name + "</a>");
        $date.html(event_date);
        $time.html(event_time);
        $location.html(event.fields.location);

        function to12Hour(time){
            var re = /^(\d\d)/g;
            return time.replace(re, function(num){
                return num - 12;
            });
        }
    } 
}(jQuery));