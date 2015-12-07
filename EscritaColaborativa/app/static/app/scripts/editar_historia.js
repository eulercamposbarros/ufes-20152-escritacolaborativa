jQuery(function ($) {

    function hideAlerts() {

        $('.alert-danger').hide();
        $('.alert-success').hide();

    }

    var init = function () {

        $('.historia').change(function () {

            hideAlerts();

            $('#cod_hist').val($(this).children('option:selected').attr('id'));

        });

        $('.escritor').change(function () {

            hideAlerts();

            $('#cod_escrit').val($(this).children('option:selected').attr('id'));

            $.ajax({
                url: './validar_escritor/', // the endpoint            
                type: "GET", // http method,            
                data: {
                    cod_hist: $('#cod_hist').val(),
                    cod_escrit: $('#cod_escrit').val()
                }, // data sent with the post request
                // handle a successful response
                success: function (data) {

                    var result = JSON.parse(data);

                    if (result.acesso == 'liberado') {
                        console.log(result.acesso);
                        $('#areaHistoria').show();
                        $('.bot-enviar').show();
                    }
                    else {
                        $('#areaHistoria').hide();
                        $('.bot-enviar').hide();
                        $('#errorMessage').show();
                        $('#errorMessage label').text(result.message)
                    }

                },
                // handle a non-successful response
                error: function (xhr, errmsg, err) {
                    // redirecionar para página de erro
                    alert('Acho que tivemos um problema.\nFavor entrar em contato com o administrador do sistema');
                }
            });

        });

    };

    init();

});