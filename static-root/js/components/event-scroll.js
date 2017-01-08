"use strict";
(function($){
    var $headers = Array.prototype.slice.call(document.querySelectorAll('.day-title')),
        header_tops = $headers.map(function(header){
            return { element: $(header), top: Math.round($(header).offset().top)}
        }),
        tops_only = header_tops.map(function(item){return item.top;});
    clear_headers();    

    window.addEventListener('scroll', function(){
        clear_headers();
        var target = get_current_header(window.scrollY);   
        if(target){
            target.addClass("sticky");  
        } 
    });

    function clear_headers(){
        $(".day-title.sticky").removeClass('sticky');
    }
    
    function get_current_header(window_top){
        function get_element_height(index){
            for (; index >= 0; index--){
                if (window_top > header_tops[index].top){
                    return header_tops[index].element;
                }
                get_element_height(index - 1);
            }
            return null;
        };    
        var element = get_element_height(header_tops.length -1);
        return element;
    }
}(jQuery));