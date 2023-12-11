$(document).ready(function() {
    var startTime = new Date();
  
    // Capture the start time when the page loads
    $(window).on('beforeunload', function() {
      var endTime = new Date();
      var duration = endTime - startTime;
      
      //var diff = Math.abs(endTime - startTime);
      //var minutes =  Math.floor((diff/1000)/60); //duration in minutes
      
      
      
      // Submit the data to the Django backend
      $.ajax({
        type: 'POST',
        url: 'track-page',  // Replace with your Django URL for time tracking
        data: {
          page_name: window.location.pathname,
          start_time: startTime.toISOString(),
          end_time: endTime.toISOString(),
          duration: duration
        }
      });
    });
  });
  