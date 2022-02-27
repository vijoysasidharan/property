$(function(){
    "use strict";
    $("#register-form").submit(function (e){
        e.preventDefault();
        var serializedData = $(this).serialize();
        $.ajax({
            type: 'POST',
            url: "/account/register/",
            data: serializedData,
            success: function (response) {
                if(response.trim() == 'success'){
                    $("#register-form")[0].reset();
                    toastr.success('Success', 'You have registered successfully.', {timeOut: 10000});
                }else{
                    toastr.error('Failed', response, {timeOut: 10000});
                }
            },
            error: function (response) {
                alert(response);
            },
            beforeSend: function(){
                $(".btn-register").html("<span class='spinner-border spinner-border-sm' role='status' aria-hidden='true'></span> Loading...");
            },
            complete: function(){
                $(".btn-register").html('REGISTER');
            }
        });
    });

    $("#login-form").submit(function (e){
        e.preventDefault();
        var serializedData = $(this).serialize();
        $.ajax({
            type: 'POST',
            url: "/account/login/",
            data: serializedData,
            success: function (response) {
                if(response.trim() == 'success'){
                    window.location = '/'
                }else{
                    toastr.error('Failed', response, {timeOut: 10000});
                }
            },
            error: function (response) {
               alert(response)
            },
            beforeSend: function(){
                $(".btn-login").html("<span class='spinner-border spinner-border-sm' role='status' aria-hidden='true'></span> Loading...");
            },
            complete: function(){
                $(".btn-login").html('LOGIN');
            }
        });
    });
})