  $(document).ready(function(){

//https://forum.jquery.com/topic/how-to-load-different-page-content-using-jquery-ajax

    $('a').click(function(e) {
        e.preventDefault(); // stops the default action of clicking on the link
        var pageToLoad = $(this).attr('href'); // gets the href of the clicked link
        //window.alert(pageToLoad);
        $('#page').load(pageToLoad); // loads the remote page into the content div without refresh
    });


  });
