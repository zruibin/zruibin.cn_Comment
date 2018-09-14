/*
 * comment.js
 *
 * Created by ruibin.chow on 2018/09/13.
 * Copyright (c) 2018年 ruibin.chow All rights reserved.
 */


function changeLinkLocation () 
{
    var w = document.documentElement.clientWidth;
    // console.log('screen.width:%f', w);
    var linkPcCss = 'background-color: #f8f8f8; width: 150px; margin: 0px 0px; padding: 10px 10px; border: 1px solid #eee; ' + 
                          'position: fixed;right: 5%; top: 10%; font-size: 16px; z-index: 1030; min-height: 50px;'; // +
    var linkMobileCss = 'background-color: #f8f8f8; margin-left: auto; margin-right: auto; margin-bottom: 10px;' + 
                              'padding-left: 10px; padding-right: 10px; border: 1px solid #eee; position: inherit; max-width: 800px;';
    var linkBlogCss = 'padding-left: 10px;';
    var link = document.getElementById('link');
    var linkBlog = getElementsClass("link_blog")
    if (w>= 1200 ) { 
        link.style.cssText = linkPcCss;
    } else {
        link.style.cssText = linkMobileCss;
    }
    for(var i=0;i<linkBlog.length;i++){ 
            linkBlog[i].style.cssText = linkBlogCss;
    }
}
