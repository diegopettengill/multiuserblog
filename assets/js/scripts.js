$(document).ready(function () {

    /* summernote editor */
    $('.summernote').summernote({
        minHeight: 300
    });

    /* comments form */
    $('.comment-form').ajaxForm({
        clearForm: true,
        success: function (response) {

            if (response.type == "error") {
                alert(response.message);
            } else {

                var html = ""
                html += '<div class="comment-item">'
                html += '<div class="comment-author">';
                html += response.comment.author;
                html += ' </div>';
                html += '<div class="comment-datetime">';
                html += response.comment.time;
                html += '</div>';
                html += '<p id="comment-text-'+response.comment.id+'">';
                html += response.comment.text;
                html += '</p>';
                html+= '<div class="comment-actions">';
                html+= '<a href="javascript:void(0)" data-comment-id="'+response.comment.id+'"';
                html+= '           class="btn btn-outline edit-comment">Edit</a>';
                html+= ' <a href="javascript:void(0)" data-comment-id="'+response.comment.id+'"';
                html+= '          class="btn btn-outline delete-comment">Delete</a>';
                html+= '</div>';
                html += '</div>';

                if (response.editing) {
                    $("#comment-text-" + response.comment.id).html(response.comment.text);
                    $("#modal-edit-comment").modal('hide');
                } else {
                    $(".comments-list").prepend(html);
                }


            }
        }
    });

    /**
     * Like post
     */
    $('.like-post').click(function () {

        var elem = $(this);
        var pid = $(this).attr("data-post-id");
        var total_likes = parseInt($(this).find("span").text());

        $.post("/post/like", {pid: pid}, function (response) {

            if (response.type == "success") {

                if (response.action == "like") {
                    elem.find("span").text(total_likes + 1);
                    elem.addClass("post-liked");
                } else {
                    elem.find("span").text(total_likes - 1);
                    elem.removeClass("post-liked");
                }

            } else {
                alert(response.message);
            }

        });

    });

    /**
     * Edit comment
     */
    $("body").on('click', '.edit-comment', function () {

        var comment_id = $(this).attr("data-comment-id");

        $.get("/comments/" + comment_id, function (response) {

            if (response.type == "success") {

                $("#modal-comment-id").val(response.comment.id);
                $("#modal-comment-text").val(response.comment.text)

                $('#modal-edit-comment').modal('show');

            } else {
                alert(response.message);
            }


        });

    });

    /**
     * Delete comment
     */
    $("body").on('click', '.delete-comment', function () {

        var comment_id = $(this).attr("data-comment-id");

        var comment_wrapper = $(this).parent().parent();

        if (confirm("You really want to delete this comment?")){

            $.get("/comments/" + comment_id + "/delete", function (response) {

                console.log(response)

                if (response.type == "success") {

                    comment_wrapper.slideUp('fast');

                } else {
                    alert(response.message);
                }

            });

        }


    });

});