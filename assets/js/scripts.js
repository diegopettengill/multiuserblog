$(document).ready(function () {

    /* comments form */
    $('#comment-form').ajaxForm({
        clearForm: true,
        success: function(response) {
            console.log(response);
        }
    });

});