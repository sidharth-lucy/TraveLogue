$('.like_post').click(function(){
    
    var post_id = $(this).attr('post_id');
    // console.log(post_id);
    // var elm = $(this)
    var strid = post_id.toString();
    $.ajax({
        type:'GET',
        url:'/like-post',
        data:{
            post_id:post_id
        },
        success: function(data){
            // console.log(data.likes);
            document.getElementById(strid).innerText = data.likes;
            // document.getElementById('lk').innerText = data.likes;
        }
    })

})




// $('.plus-cart').click(function(){
//     var id = $(this).attr("productId").toString();
//     // console.log(id)
//     var eml = this.parentNode.children[2];
//     $.ajax({
//         type:'GET',
//         url:'/pluscart',
//         data:{
//             prod_id: id
//         },

//         success: function(data){
//             // console.log(data);
//             eml.innerText= data.quantity;
//             document.getElementById('amount').innerText = data.amount;
//             document.getElementById('sip-charge').innerText = data.shipping_charge;
//             document.getElementById('totalcost').innerText = data.total_cost;
//         }
//     })
// })


