$(document).ready(function () {
  let code = $('INPUT#language_code').val();
  $('INPUT#btn_translate').click(function () {
    $.get('https://www.fourtonfish.com/hellosalut/hello/?lang=${code}',
    function (data) {
      $('DIV#hello').text(data.hello)
    });
  });
});
