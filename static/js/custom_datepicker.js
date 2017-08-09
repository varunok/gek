/**
 * Created by varunok on 20.04.17.
 */
$(document).ready(function() {
    $('input.daterange').daterangepicker({
        singleDatePicker: true,
        "opens": "center",
        locale: {
            format: 'DD.MM.YYYY',
            "applyLabel": "Применить",
            "cancelLabel": "Отменить",
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

      $('input[name="when_create"]').daterangepicker({
          autoUpdateInput: false,
          locale: {
              format: 'DD.MM.YYYY',
              "applyLabel": "Применить",
                "cancelLabel": "Отменить",
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
          }
      });

      $('input[name="when_create"]').on('apply.daterangepicker', function(ev, picker) {
          $(this).val(picker.startDate.format('DD.MM.YYYY') + ' - ' + picker.endDate.format('DD.MM.YYYY'));
      });

      $('input[name="when_create"]').on('cancel.daterangepicker', function(ev, picker) {
          $(this).val('');
    });
})