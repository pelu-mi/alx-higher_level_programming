$(document).ready(function () {
  $('INPUT#btn_translate').click(translate());
  $('INPUT#language_code').keyup(function (event) {
    if (event.keyCode == 13) {
      translate();
    }
  });

  function translate() {
    let code = $('INPUT#language_code').val();
    $.get('https://www.fourtonfish.com/hellosalut/hello/?lang=${code}',
    function (data) {
      $('DIV#hello').text(data.hello)
    }
});
