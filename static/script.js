function search() {
  // Declare variables
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("search");
  filter = input.value.toUpperCase();
  table = document.getElementById("chapters");
  tr = table.getElementsByTagName("tr");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
	data =  tr[i].getElementsByTagName("td");
	for (j = 0; j < data.length; j++) {
    	td = tr[i].getElementsByTagName("td")[j];
    	if (td) {
      		txtValue = td.textContent || td.innerText;
      		if (txtValue.toUpperCase().indexOf(filter) > -1) {
        		tr[i].style.display = "";
				break;
	      	} else {
   	     		tr[i].style.display = "none";
    	  	}
		}
    }
  }
}
