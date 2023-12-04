$('.btn-reply').on('click', function(){
    var postId = $(this).data('post')
    $('#respondendoDiv').removeClass('hidden')
    $('#id_respondendo').val(postId)
    var postContent = $(`#post-${postId}`).text()
    $('#postRespondendo').empty()
    $('#postRespondendo').append(`${postContent.slice(0,1000)}...`)

})

$('#removeReply').on('click', function(){
    console.log('Removendo')
    $('#respondendoDiv').addClass('hidden')
    $('#id_respondendo').val('')
    $('#postRespondendo').empty()
})