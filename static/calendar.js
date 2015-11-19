
jQuery('#time-selector select').on('change', function() {
  validate();
});

jQuery('.calendar-day').on('click', function(e) {

  var rowPitch = 40; // Each hour takes 40 vertical pixels.
  var startingHour = 8; // 8am start of day

  var delta = e.clientY - this.offsetTop; // pixels
  var minutes = delta / rowPitch * 60;
  var quarterHours = Math.floor(minutes / 15);

  var hours = startingHour + Math.floor(quarterHours / 4);
  var minutes = (quarterHours % 4) * 15;

  // Fill in form elements
  if (hours > 12) {
    jQuery('[name=hour]').val(hours - 12);
    jQuery('[name=ampm]').val('pm');
  } else {
    jQuery('[name=hour]').val(hours);
    jQuery('[name=ampm]').val('am');
  }
  jQuery('[name=minute]').val(minutes);

  validate();
});

jQuery('#time-selector').on('submit', function() {
  var data = jQuery(this).serialize();
  jQuery.post('/schedule', data, function(response) {
    // Hack. AppEngine datastore isn't strongly consistent unless you do all the
    // ancestor entity group stuff.
    setTimeout(function() {
      window.location.reload();
    }, 500);
  });
  return false;
});

function validate() {
  var hours = Number(jQuery('[name=hour]').val());
  if (jQuery('[name=ampm]').val() == 'pm') {
    hours += 12;
  }
  var minutes = jQuery('[name=minute]').val();
  var minuteStamp = Number(hours) * 60 + Number(minutes);

  var available = availability.some(function(block) {
    var start = block.start_hour * 60 + block.start_minute;
    var end = start + block.duration_minutes;
    return minuteStamp >= start && (minuteStamp + 60) <= end;
  });

  var conflict = appointments.some(function(block) {
    var start = block.start_hour * 60 + block.start_minute;
    var end = start + block.duration_minutes;
    var intersect = start < minuteStamp + 60 && minuteStamp < end;
    return intersect;
  });

  var valid = available && !conflict;
  jQuery('#time-selector input[type=submit]').attr('disabled', !valid);
}
