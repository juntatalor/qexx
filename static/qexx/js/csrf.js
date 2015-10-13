/**
 * Created by Сергей on 15.02.2015.
 */

function csrfSafeMethod(method) {
    // Методы, которые не требуют CSRF защиты
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$(document).ready(function () {

    var csrftoken = $(":input[name='csrfmiddlewaretoken']").val();

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});
