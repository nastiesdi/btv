// PopUp Form and thank you popup after sending message
var $popOverlay = $(".popup-overlay");
var $popWindow = $(".popWindow");
var $subscribeWindow = $(".subscribe_window");
var $popThankYouWindow = $(".thank_you_window");
var $popClose = $(".close-btn");
var $popUp = $('#popup');


$('document').ready(function(){
    $popOverlay.hide();
    $popWindow.hide();
    console.log('open page');
});


$popUp.on('click', function(){
//    $popOverlay.addClass('$popup-overlay')
    $popOverlay.fadeIn();
    $popWindow.fadeIn();
    $popThankYouWindow.remove()
    console.log('click')

});

$(function() {
  // Close Pop-Up after clicking on the button "Close"
  $popClose.on("click", function() {
    $popOverlay.fadeOut();
    $popWindow.fadeOut();
  });

  // Close Pop-Up after clicking on the Overlay
  $(document).on("click", function(event) {
    if ($(event.target).closest($popWindow).length) return;
//    $popOverlay.fadeOut();
//    $popWindow.fadeOut();
    event.stopPropagation();
    console.log('here2')
  });

  // Form Subscribe
  $(".subscribe-form").submit(function() {
    var th = $(this);
    $.ajax({
      type: "POST",
      url: 'url ',
      data: th.serialize()
    }).done(function() {
      // после успешной отправки скрываем форму подписки и выводим окно с благодарностью за заполнение формы
      $subscribeWindow.fadeOut();
      $popThankYouWindow.fadeIn();
      // используем куки на 30 дней, если человек заполнил форму
      // для куки обязательно должен быть подключен jquery.cookie.min.js
      //$.cookie('hideTheModal', 'true', { expires: 30 });
      // очищаем форму
      setTimeout(function() {
        th.trigger("reset");
      }, 1000);
    });
    return false;
  });
});

// используйте этот код, если нужно появление формы без куки
$(window).load(function() {
  setTimeout(function() {
    $popOverlay.fadeIn();
    $subscribeWindow.fadeIn();
  }, 2000);
});