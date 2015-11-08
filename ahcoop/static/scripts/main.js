$(function() {


    // Submit post on submit
	
	$('#CadastroProduto').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        create_Produto();
    });
	
	
    $('#post-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        create_post();
    });
	
	$('#formPesquisaProd').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        pesquisa_Produto();
    });
	
	$('#comentariosMissao').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        create_comentario();
    });
	
	$('#adicionaTipoMissao').on('submit', function(event){
		event.preventDefault();
        console.log("form submitted!")  // sanity check
        create_tipoMissao();
    });
	
	$('#adiciona_Missao').on('submit', function(event){
		event.preventDefault();
        console.log("form submitted!")  // sanity check
        create_Missao();
    });
	
	$("#adicionaItem").on('click', 'a[id^=botao-Adicionar-]', function(){
        var post_primary_key = $(this).attr('id').split('-')[2];
        console.log(post_primary_key) // sanity check
		adiciona_Item(post_primary_key);
        
		
    });

    // Delete post on click
    $("#talk").on('click', 'a[id^=delete-post-]', function(){
        var post_primary_key = $(this).attr('id').split('-')[2];
        console.log(post_primary_key) // sanity check
        delete_post(post_primary_key);
    });
	
	// Delete post on click
    $("#deletarProduto").on('click', 'a[id^=delete-produto-]', function(){
		
        var post_primary_key = $(this).attr('id').split('-')[2];
        console.log(post_primary_key) // sanity check
        delete_produto(post_primary_key);
		
    });

    // AJAX for posting
	
	function adiciona_Item(post_primary_key) {
        console.log("create post is working!") // sanity check
		
        $.ajax({
			
            url : "/adicionaItem/", // the endpoint
            type : "POST", // http method
            data : {formIDProd : $('#formIDProd'+post_primary_key).val(), formQuantidade : $('#formQuantidade'+post_primary_key).val(), IDPedido : $('#IDMissao').val()}, // data sent with the post request
            
			// handle a successful response
			
            success : function(json) {
                console.log(json); // log the returned json to the console
                $("#mostraMessage"+json.id).html("<div id='mostraMessage"+json.id+"' class='alert alert-dismissable alert-"+json.tipo+"'><button type='button' class='close' data-dismiss='alert'>×</button>" + json.message+ "</div>");
				$("#totalDeItens").html("<span id='totalDeItens' class='badge'>"+json.totalDeItens+"</span>");
            },
            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    };
	
	function create_Produto() {
        console.log("create post is working!") // sanity check
		
        $.ajax({
			
            url : "/create_Produto/", // the endpoint
            type : "POST", // http method
            data : { descricao : $('#descricao').val(), preco : $('#preco').val(), fabricante : $('#fabricante').val() , peso : $('#peso').val() , calorias : $('#calorias').val() ,
					url : $('#url').val(), estoque : $('#estoque').val(), medidas : $('#medidas').val(), ativo : $('#ativo').val(), selectDept : $('#selectDept').val(),
					selectSec : $('#selectSec').val(),componentes : $('#componentes').val(), origem : $('#origem').val()}, // data sent with the post request
            // handle a successful response
			
            success : function(json) {
                $('#CadastroProduto').val(''); // remove the value from the input
                console.log(json); // log the returned json to the console
                
            },
            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    };
	
	function atualiza_Secoes(id) {
        console.log("create post is working!") // sanity check
		
        $.ajax({
			
            url : "/atualizaSecoes/", // the endpoint
            
            data : { departamentoID : id}, // data sent with the post request
            // handle a successful response
			
            success : function(json) {
                $('#CadastroProduto').val(''); // remove the value from the input
                console.log(json); // log the returned json to the console
                
            },
            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    };
	
	function pesquisa_Produto() {
        console.log("create post is working!") // sanity check
		
        $.ajax({
			
            url : "/pesquisaProduto/", // the endpoint
            type : "POST", // http method
            data : { descricao : $('#pesquisaProd').val()}, // data sent with the post request
            // handle a successful response
			
            success : function(json) {
                $('#pesquisaProd').val(''); // remove the value from the input
                console.log(json); // log the returned json to the console
                console.log("success"); // another sanity check
				
				
				
            },
            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    };
	
	function create_comentario() {
        console.log("create post is working!") // sanity check
		
        $.ajax({
			
            url : "/insereComentarioMissao/", // the endpoint
            type : "POST", // http method
            data : { comentario : $('#comentario').val(), IDMissao : $('#IDMissao').val() }, // data sent with the post request
            // handle a successful response
			
            success : function(json) {
                $('#comentario').val(''); // remove the value from the input
                console.log(json); // log the returned json to the console
                $("#listaComentarios").prepend("<div id='post-"+json.id+"' class='alert alert-dismissable alert-warning'><strong>"+json.texto+"</strong> <br><span class='label label-default'>"+json.nomeUser+" - "+json.sent+"</span></div>");
				
                console.log("success"); // another sanity check
            },
            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    };
	
	function create_Missao() {
        console.log("create post is working!") // sanity check
		
        $.ajax({
			
            url : "/adicionaMissao/", // the endpoint
            type : "POST", // http method
            data : { nomeMissao : $('#nomeMissao').val(), focoMissao : $('#focoMissao').val(), descDetalhada : $('#descDetalhada').val(), IDMissao : $('#IDMissao').val()}, // data sent with the post request
            // handle a successful response
			
            success : function(json) {
                $('#nomeMissao').val('');
				$('#focoMissao').val('');
				$('#descDetalhada').val('');// remove the value from the input
                console.log(json); // log the returned json to the console	
				$('#results').html("<div class='alert-box alert radius' data-alert> Missão adicionada/editada com Sucesso! <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText);				
                
            },
            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    };
	
    function create_post() {
        console.log("create post is working!") // sanity check
		
        $.ajax({
			
            url : "/create_post/", // the endpoint
            type : "POST", // http method
            data : { the_post : $('#the_post').val() }, // data sent with the post request
            // handle a successful response
			
            success : function(json) {
                $('#post-text').val(''); // remove the value from the input
                console.log(json); // log the returned json to the console
                $("#talk").prepend("<li id='post-"+json.id+"'><strong>"+json.nome+"</strong>");
                console.log("success"); // another sanity check
            },
            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    };

    // AJAX for deleting
    function delete_post(post_primary_key){
        if (confirm('are you sure you want to remove this post?')==true){
            $.ajax({
                url : "delete_post/", // the endpoint
                type : "DELETE", // http method
                data : { postpk : post_primary_key }, // data sent with the delete request
                success : function(json) {
                    // hide the post
                  $('#post-'+post_primary_key).hide(); // hide the post on success
                  console.log("post deletion successful");
                },

                error : function(xhr,errmsg,err) {
                    // Show an error
                    $('#results').html("<div class='alert-box alert radius' data-alert>"+
                    "Oops! We have encountered an error. <a href='#' class='close'>&times;</a></div>"); // add error to the dom
                    console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                }
            });
        } else {
            return false;
        }
    };
	
	function delete_produto(post_primary_key){
		$.ajax({
			url : "/deleta_produto/", // the endpoint
			type : "DELETE", // http method
			data : { postpk : post_primary_key }, // data sent with the delete request
			success : function(json) {
				// hide the post
			  $('#linhasItens'+post_primary_key).hide(); // hide the post on success			  			  
			  $('#totalItens').html("<div id='totalItens'><span class='label label-warning'><b>Valor Total do Carrinho: "+json.total+"</b></span></div><br>"); 
			  $('#totalDeItens').html("<span id='totalDeItens' class='badge'>"+json.totalItens+"</span>");								
			  console.log("post deletion successful");
			},

			error : function(xhr,errmsg,err) {
				// Show an error
				$('#results').html("<div class='alert-box alert radius' data-alert>"+
				"Oops! We have encountered an error. <a href='#' class='close'>&times;</a></div>"); // add error to the dom
				console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
			}
		});
    };


    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});