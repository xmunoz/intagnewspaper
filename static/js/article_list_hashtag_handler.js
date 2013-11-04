var hash_toolkit = {},
    default_year = "2012";

$(function() {
    var onload_hash = window.location.hash,
        set_year = default_year;

    if ( onload_hash == "" ) {
        window.location.hash = set_year; 
    } else {
        set_year = onload_hash.substring(1)
    }

    hash_toolkit = {
        el  : null,
        siblings    : null,
        tab_el  : null,
        tab_siblings    : null,
        year_display_el    : $(".hash-year"),
        year    : set_year
    }

    update_toolkit(hash_toolkit, set_year);
    hash_action(hash_toolkit);
})

$(window).on("hashchange", function(ev) {
    hash_toolkit.year = window.location.hash.substring(1)
    update_toolkit( hash_toolkit, window.location.hash.substring(1) )
    hash_action(hash_toolkit);
})

var hash_action = function(hash_obj) {
    hash_obj.year_display_el.html( hash_obj.year )
    hash_obj.el.addClass("display");
    hash_obj.siblings.removeClass("display");
    hash_obj.tab_el.addClass("selected");
    hash_obj.tab_siblings.removeClass("selected");
}

var update_toolkit = function (hash_obj, current_hash) {
    hash_obj.el = $(".archive-loop[year='" + current_hash + "']");
    hash_obj.siblings = $(".archive-loop").not("[year='" + current_hash + "']");
    hash_obj.tab_el = $(".menu-tab[href='#" + current_hash + "']");
    hash_obj.tab_siblings = $(".menu-tab").not("[href='#" + current_hash + "']");
    hash_obj.year = current_hash
}
