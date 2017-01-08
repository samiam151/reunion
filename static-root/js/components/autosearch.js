"use strict";
(function($){
    var $input = $(".auto-search-input"),
        $results_ul = $('.auto-search-results'),
        numToStartSearch = 2;
    
    $results_ul.hide();
    $input.on('keyup', function(e){
        if($input.val().length >= numToStartSearch){
            $results_ul.show();
            autocomplete(e.target.value);
        } else {
            $results_ul.hide();
        }   
    });

    $(window).on('click', function(e){
        if ($(e.target)[0] !== $input[0] || $(e.target)[0] !== $results_ul[0]){
            $results_ul.hide();
        }
    });

    function autocomplete(term){
        $.get('/rsvp/json_rsvp_all', function(data){
            // Clean the data
            var results = find_matches(clean_data(data), term);
            // Populate the UL
            full_ul(results);         
        });
    }

    function clean_data(data){
        // Returns an ARRAY of OBJECT LITERALS
        return data.map(function(item){
            var neatResults = item.fields;
            neatResults['pk'] = item.pk;
            return neatResults;
        });
    }

    function find_matches(results, term){
        return results.filter(function(result){
            return result.name.toLowerCase().includes(term.toLowerCase());
        });
    }

    function full_ul(jsonResults){
        if($results_ul.children().length > 0){
            $results_ul.html("");
        }
        
        if(jsonResults){
            jsonResults.forEach(function(result){
                $results_ul.append("<li class='auto-search-result'><a href='/rsvp/detail/" + result.pk + "'>" + result.name + "</a></li>");
            });
        } else {
            $results_ul.hide();
        }      
    }
}(jQuery));