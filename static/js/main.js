/**
 * Created by User on 20.04.2015.
 */

(function() {

    var app = {

        // -- инициализация при загрузке js
        initialize : function () {
            var _this = this;

            _this.setUpListeners();

        },
         // -- инициализация при загрузке js

        // -- обработчик событий над DOM элементами на странице
        setUpListeners: function () {

            // -- нажата кнопка добавления студента
            $('.btn__add-student').on('click', app.sendStudent);
            // -- нажата кнопка заказа услуги

        },
        // -- обработчик событий над DOM элементами на странице

        // -- функции вызываемые из setUpListeners ===============

         // -- отправка данных из модальной формы обратного звонка
        sendStudent: function (e) {
            e.preventDefault();

            var form = $('.form_add-student'),
                submitBtn =  $(this);

            submitBtn.button('loading');

            //submitBtn.attr({disabled: 'disabled'}); // защита от повторного нажатия + показываем загрузчик
            var str = form.serialize();

            console.log(str);
            $.ajax({
                type: "POST",
                url: "/student/new/",
                dataType: 'json',
                data: str
            }).success(

                alert('OK')
            ).always(function(){
                //submitBtn.removeAttr('disabled');
                submitBtn.button('reset')
            });

        },
        // -- отправка данных из модальной формы обратного звонка

        // -- отправка данных из модальной формы
        //sendOrderData: function (e) {
        //    e.preventDefault();
        //
        //    var form = $(this).parents('.modal-content').find('.send-order-data-form'),
        //        str = '',
        //        submitBtn = $(this).parents('.modal-content').find('.do-order-btn'),
        //        checkBoxes = $(this).parents('.modal-content').find(".checkbox-userv"),
        //        valPhone = $(this).parents('.modal-content').find('#inputPhone').val(),
        //        rePhone = /^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$/,
        //        valEmail =  $(this).parents('.modal-content').find('#inputEmail').val(),
        //        reEmail = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
        //
        //    $.each( checkBoxes , function(index, val) {
        //        var currentItem = $(val);
        //            if (currentItem.prop("checked")) {
        //                app.checkValue = app.checkValue + 1
        //            }
        //    });
        //
        //    if ( app.checkValue === 0 ) {
        //        $(this).parents('.modal-content').find('#error-div').removeClass('bg-success').addClass('bg-danger').text('Для заказа нужно выбрать хотя бы одну услугу!');
        //        return false
        //    }
        //
        //    if(valPhone.length === 0){
        //        $(this).parents('.modal-content').find('#error-div').removeClass('bg-success').addClass('bg-danger').text('Необходимо ввести номер телефона!');
        //        return false;
        //    } else {
        //        var validPhone = rePhone.test(valPhone);
        //        if (!validPhone) {
        //            $(this).parents('.modal-content').find('#error-div').removeClass('bg-success').addClass('bg-danger').text('Необходимо ввести правильный номер телефона!');
        //            return false;
        //        }
        //    }
        //    valPhone = valPhone.replace(/[+()-]/g, "");
        //
        //    if (valEmail.length != 0) {
        //        var validEmail = reEmail.test(valEmail);
        //        if (!validEmail) {
        //            $(this).parents('.modal-content').find('#error-div').removeClass('bg-success').addClass('bg-danger').text('Адрес электронной почты не соотвествует формату. Введите правильный email!');
        //            return false;
        //        }
        //    }
        //
        //    submitBtn.attr({disabled: 'disabled'}); // защита от повторного нажатия + показываем загрузчик
        //    str = form.serialize();
        //    str = str + '&inputPhone=' + valPhone;
        //
        //    app.checkValue = 0;
        //    $.ajax({
        //        type: "POST",
        //        url: "/submit",
        //        dataType: 'json',
        //        data: str
        //    }).done(
        //        $(this).parents('.modal-content').find('#error-div').removeClass('bg-danger').addClass('bg-success').text('Ваша заявка принята! В ближайшее время с вами свяжется наш менеджер.')
        //    ).always(function(){
        //        submitBtn.removeAttr('disabled');
        //    });
        //},
        // -- отправка данных из модальной формы

        // -- пустая функция чтоб не было ошибки с запятой у сетаплистенеров
        someFunction: function () {}
        // -- пустая функция чтоб не было ошибки с запятой у сетаплистенеров

        // -- функции вызываемые из setUpListeners ===============

    }

    app.initialize();




}());