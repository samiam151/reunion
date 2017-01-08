"use strict";
(function($){
    $.get('/events/json_events_all', function(events){
        // "date < date2" = date1 comes BEFORE date2
        populate_div(getFirstEvent(events));
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
            if(+time.split(":")[0] > 12){
                var new_time = +time.split(":")[0] - 12;
                var old_time= [time.split(":")[0], time.split(":")[1]];
                old_time[0] = new_time;
                return old_time.join(":") + " PM";
            }
            return new_time;
        }
    } 
}(jQuery));