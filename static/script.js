const data_form = document.getElementById('form');
if (data_form !== null) {
    data_form.addEventListener('submit', send_source_text_to_api);
}


function send_source_text_to_api(event) {
  event.preventDefault();

  const source_text = data_form.querySelector('[name="source_text"]');

  update_html_content_by_tag('.data-container','<img class="loading-result" src="static/loading.gif">')
  setTimeout(() => {}, 500);

  const params_data = {
    source_text: source_text.value
  };

  let new_content = `
    <p class="text-error">Что-то пошло не так!</p>
    <a class="ri-button" href="/">ВЕРНУТЬСЯ НА ГЛАВНУЮ</a>
  `

  $.ajax({
	url: '/processing',
	method: 'post',
	dataType: 'json',
	data: params_data,
	complete: function(data) {
        let answer_data = JSON.parse(data.responseText);
        if (answer_data['status'] === true) {
            update_html_content_by_tag('.data-container', answer_data['html']);
        } else {
            update_html_content_by_tag('.data-container', answer_data['html']);
        }
	}, error: function (jqXHR, exception) {
      if (jqXHR.status === 0) {
          console.log('[API JS] Not connect. Verify Network.');
          update_html_content_by_tag('.data-container', new_content);
      } else if (jqXHR.status === 404) {
          console.log('[API JS] Requested page not found (404).');
          update_html_content_by_tag('.data-container', new_content);
      } else if (jqXHR.status === 500) {
          console.log('[API JS] Internal Server Error (500).');
          update_html_content_by_tag('.data-container', new_content);
      } else if (exception === 'parsererror') {
          console.log('[API JS] Requested JSON parse failed.');
          update_html_content_by_tag('.data-container', new_content);
      } else if (exception === 'timeout') {
          console.log('[API JS] Time out error.');
          update_html_content_by_tag('.data-container', new_content);
      } else if (exception === 'abort') {
          console.log('[API JS] Ajax request aborted.');
          update_html_content_by_tag('.data-container', new_content);
      } else {
          console.log('[API JS] ' + 'Uncaught Error. ' + jqXHR.responseText);
          update_html_content_by_tag('.data-container', new_content);
      }
    }
  });
}

function update_html_content_by_tag(selector, new_content) {
  try {
    $(selector).fadeOut(200, function () {
    $(this).html(new_content).fadeIn(100);
  })
  } catch (e) {
    console.log('[JS Engine] Error JS func - "update_html_content_by_tag"!')
  }
}