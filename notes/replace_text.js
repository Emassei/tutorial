
<script>
var guy = $('#is-rollover-investor-container > label');
h = guy.html();
guy.html(h.replace('Previous investor in projects sponsored by Arbor Crowd.', 'Previous investor in projects sponsored by Arbor Crowd within 90 days.'));
</script>
<script>
lineItem = $('#property_listing > div.col-md-4.summary-items > div > table > tbody > tr:nth-child(1) > td:nth-child(2)')
html = lineItem.html()
lineItem.html(html.replace('7350 Campbellton Rd SW, Atlanta, GA 30331','7350 Campbellton Rd SW<br> Atlanta, GA 30331'))
</script>



