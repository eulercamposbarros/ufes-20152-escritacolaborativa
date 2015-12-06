jQuery(function ($) {

    var atividade = function () {

        $('.historia').change(function (e) {

            e.preventDefault();

            var historia_selecionada = $(this).children('option:selected').attr('id');

            if (historia_selecionada != 0) {

                $('#cod_hist').val(historia_selecionada);

                listar_historia();
            }

        });
    };


    // Listar História

    var listar_historia = function () {

        $.ajax({
            url: './listar_interacao_historia/', // the endpoint            
            type: "GET", // http method,            
            data: {
                cod_hist: $('#cod_hist').val()                
            }, // data sent with the post request
            // handle a successful response
            success: function (data) {

                $('.conteudo-historia').html("");

                if (data != undefined && data != null) {
                    debugger;

                    data = jQuery.parseJSON(data);
                    
                    var html = "<h1>" + data[0].titulo + "</h1>";

                    html += "<p>" + data[0].primeiro_paragrafo + "</p>";

                    for (var i = 0; i < data.length; i++) {

                        html += "<p>" + data[i].interacao + "</p>"
                    }

                    $('.conteudo-historia').html(html);
                }
            },
            // handle a non-successful response
            error: function (xhr, errmsg, err) {
                // redirecionar para página de erro
                alert('Acho que tivemos um problema.\nFavor entrar em contato com o administrador do sistema');

            }
        });


    };


    var init = function () {

        atividade();
    
    };

    init();

});