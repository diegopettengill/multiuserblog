$(document).ready(function () {

    /* summernote editor */
    $('.summernote').summernote({
        minHeight: 300,
    });

    /* comments form */
    $('#comment-form').ajaxForm({
        clearForm: true,
        success: function(response) {

            if(response.type == "error"){
                alert(response.message);
            }else{

                var html = ""
                html += '<div class="comment-item">'
                html += '<div class="comment-author">';
                html += response.comment.author;
                html += ' </div>';
                html +=  '<div class="comment-datetime">';
                html +=  response.comment.time;
                html += '</div>';
                html += '<p>';
                html += response.comment.text;
                html += '</p>';
                html += '</div>';

                $(".comments-list").prepend(html);

            }
        }
    });

    $('.like-post').click(function(){

        var elem = $(this);
        var pid = $(this).attr("data-post-id");
        var total_likes = parseInt($(this).find("span").text());

        $.post("/post/like", {pid : pid}, function(response){

            if(response.type == "success"){

                if(response.action == "like"){
                    elem.find("span").text(total_likes+1);
                    elem.addClass("post-liked");
                }else{
                    elem.find("span").text(total_likes-1);
                    elem.removeClass("post-liked");
                }

            }

        });


    });

});