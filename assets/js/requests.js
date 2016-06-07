function setTitle(request_new_title) {
     if (document.title != request_new_title) {
          document.title = request_new_title;
     }
}

var active = true;
var repeatAjax;
function sendAjax() {
     $.getJSON('requests_json', function(data) {
          setTitle(data['requests_title']);
          var requests_list=data['requests_list'];
          var requests_list_html='';
          for (var i=0; i<requests_list.length; i++) {
              requests_list_html+='<p>'+requests_list[i]+'</p>'
          }
          $('#requests_list').html(requests_list_html);
     })
     .always(function() {
        if (!active) {
            repeatAjax = setTimeout(sendAjax, 5000);
        }
     });
}

$(window).focus(function(){
    active = true;
    clearTimeout(repeatAjax);
    $.getJSON('requests_json', {window_state:'active'});
    setTitle("Requests");
});

$(window).blur(function(){
    active = false;
    $.getJSON('requests_json', {window_state:'inactive'});
    sendAjax();
});


