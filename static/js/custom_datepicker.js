/**
 * Created by varunok on 20.04.17.
 */
$(document).ready(function() {
    $('input.daterange').daterangepicker({
        singleDatePicker: true,
        "opens": "center",
        locale: {
            format: 'DD.MM.YYYY',
            "firstDay": 1,
            "daysOfWeek": [
                "Вс",
                "Пн",
                "Вт",
                "Ср",
                "Чт",
                "Пт",
                "Сб"
            ],
            "monthNames": [
                "Январь",
                "Февраль",
                "Март",
                "Апрель",
                "Май",
                "Июнь",
                "Июль",
                "Август",
                "Сентябрь",
                "Октябрь",
                "Ноябрь",
                "Декабрь"
            ]
        },
    });
})