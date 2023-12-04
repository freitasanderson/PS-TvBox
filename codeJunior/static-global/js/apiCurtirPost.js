$('.btn-like').on('click', function(){
    var url = $('#urlApiCurtida').val()
    var postId = $(this).data('post');
    var curtido = $(this).data('curtido');

    chamarApiCurtida(url, postId,curtido)
})

function chamarApiCurtida(url,postId) {
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

    let data = {
        'post': postId,
    }

    var response = $.ajax({
        url: url,
        type: 'post',
        data: data,
        dataType: "json",
        accept: "application/json",
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
        success: function (dados) {
            console.log(dados)
            if (dados.status){
                $(`#btn-like-${postId}`).empty();
                $(`#btn-like-${postId}`).append(`
                    <svg class="w-3 h-3 mr-1" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 22 20">
                        <path d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"/>
                    </svg>
                    Curtido
                `)
            }
            else{
                $(`#btn-like-${postId}`).empty();
                $(`#btn-like-${postId}`).append(`
                    <svg class="w-3 h-3 mr-1" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 21 20">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m11.479 1.712 2.367 4.8a.532.532 0 0 0 .4.292l5.294.769a.534.534 0 0 1 .3.91l-3.83 3.735a.534.534 0 0 0-.154.473l.9 5.272a.535.535 0 0 1-.775.563l-4.734-2.49a.536.536 0 0 0-.5 0l-4.73 2.487a.534.534 0 0 1-.775-.563l.9-5.272a.534.534 0 0 0-.154-.473L2.158 8.48a.534.534 0 0 1 .3-.911l5.294-.77a.532.532 0 0 0 .4-.292l2.367-4.8a.534.534 0 0 1 .96.004Z"/>
                    </svg>
                    Curtir
                `)
                
            }
            $(`like-${postId}`).empty();

            if (dados.curtidas.length > 0 && dados.curtidas.length == 1){
                dados.curtidas.forEach((curtida) => {
                    $(`#like-${postId}`).append(`
                        <span>
                            ${curtida.quemCurtiu.nome}
                        </span>
                    `)
                })
            }
            else if (dados.curtidas.length > 1){
                dados.curtidas.forEach((curtida) => {
                    $(`#like-${postId}`).append(`
                        <span>
                            ${curtida.quemCurtiu.nome},
                        </span>
                    `)
                })
            }

        },
        error: function (retorno) {
            console.log(retorno)
        },

    })
}