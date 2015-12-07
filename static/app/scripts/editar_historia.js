jQuery(function ($) {

    var atividade = function () {

        $('.historia').change(function (e) {
            
            e.preventDefault();

            var historia_selecionada = $(this).children('option:selected').attr('id');

            if (historia_selecionada != 0) {

                $('#cod_hist').val(historia_selecionada);
                
            }

        });
    };


    var validar_escritor = function () {
        $('#validar').click(function (e) {
            
            $.ajax({
                url: './validar_escritor/', // the endpoint            
                type: "GET", // http method,            
                data: {
                    cod_hist: $('#cod_hist').val(),
                    cod_escr: $('#cod_escr').val()
                }, // data sent with the post request
                // handle a successful response
                success: function (data) {

                    if (data == 'liberado') {
                        $('#descricao_historia').show();
                        $('.bot-enviar').show();
                    }
                    else {
                        $('#descricao_historia').hide();
                        $('.bot-enviar').hide();
                        
                    }

                },
                // handle a non-successful response
                error: function (xhr, errmsg, err) {
                    // redirecionar para página de erro
                    alert('Acho que tivemos um problema.\nFavor entrar em contato com o administrador do sistema');

                }
            });
     
            

        });
    }


    var init = function () {
        
        $('#descricao_historia').hide();
        $('.bot-enviar').hide();
        atividade();
        validar_escritor();
    };

    init();
    
});