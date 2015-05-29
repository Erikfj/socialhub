$(document).ready(function(){
// Skriv all js i mellom $doc og closing brackets!

	$(".add-points-link").click(function(event) {
		event.preventDefault();
		var topic_id = $(this).data("topicid");
		var points_element_id = "#id-points-for-topic-" + topic_id;
		$.ajax({
			method: "POST",
			url: $('#add_points_url').val() + "/" + topic_id
		})
		.done(function(data){
		var points_updated = data['points_updated'];
		$(points_element_id).html(points_updated);
		});
	});


});

