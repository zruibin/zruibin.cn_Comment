/*
 * comment.js
 *
 * Created by ruibin.chow on 2018/09/13.
 * Copyright (c) 2018年 ruibin.chow All rights reserved.
 */


var data = [
        {   "uuid":"werwfwwsdfsfdsfds",
            "name": "zruibin", 
            "content":"121212121", 
            "time":"2018-01-11 10:22",
            "replyList":[
                {"uuid":"werwfwwsdfsfdsf111", "name": "zruibin", "content":"121212121", "time":"2018-01-11 10:22"},
                {"uuid":"werwfwwsdfsfdsvs22", "name": "zruibin", "content":"133331", "time":"2018-01-11 10:22"},
                {"uuid":"w11111fdsfds", "name": "zruibin", "content":"125555521", "time":"2018-01-11 10:22"},
                {"uuid":"we00000sfds", "name": "zruibin", "content":"56666666666661", "time":"2018-01-11 10:22"},
            ]
        },

        {
            "uuid":"werwfww-----fds",
            "name": "zruibin", 
            "content":"为了进一步激发你的学习欲望, 我们想让你先看一下 TensorFlow 是如何解决一个经典的机器 学习问题的. 在神经网络领域, 最为经典的问题莫过于 MNIST 手写数字分类问题. 我们准备了 两篇不同的教程, 分别面向机器学习领域的初学者和专家. 如果你已经使用其它软件训练过许多 MNIST 模型, 请阅读高级教程 (红色药丸链接). 如果你以前从未听说过 MNIST, 请阅读初级教程 (蓝色药丸链接). 如果你的水平介于这两类人之间, 我们建议你先快速浏览初级教程, 然后再阅读高级教程", 
            "time":"2018-01-11 10:22",
            "replyList":[
                {"uuid":"999999fsfdsds", "name": "zruibin", "content":"121212121", "time":"2018-01-11 10:22"},
                {"uuid":"77666sfdsd", "name": "zruibin", "content":"133331", "time":"2018-01-11 10:22"},
            ]
        },

        {
            "uuid":"1122fff",
            "name": "zruibin", 
            "content":"121212121如何阅读一本书？如何阅读一本书？", 
            "time":"2018-01-11 10:22",
            "replyList":[
                {"uuid":"44dsfsvvvbnnm", "name": "zruibin", "content":"如何阅读一本书？如何阅读一本书？如何阅读一本书？如何阅读一本书？", "time":"2018-01-11 10:22"},
                {"uuid":"mmmlll11", "name": "zruibin", "content":"如何阅读一本书？如何阅读一本书？", "time":"2018-01-11 10:22"},
            ]
        },

        {
            "uuid":"xxxxx1111",
            "name": "zruibin", 
            "content":"如何阅读一本书？如何阅读一本书？", 
            "time":"2018-01-11 10:22",
            "replyList":[]
        },
    ];



showComment(data);

function showComment(data) {
    var commentDiv = document.getElementById("comment");
    comments = getComments(data);
    commentDiv.innerHTML = comments + getCommentPages();
}

function getComments (data) {

    comments = "";
    for (var i = 0; i < data.length; i++) {
        comment = data[i]
        comments += getComment(comment);
    };
    return comments;
}

function getComment (comment) {
    var uuid = comment["uuid"];
    var name = comment["name"];
    var content = comment["content"];
    var time = comment["time"];
    var replyList = comment["replyList"];

    var html = '<article><hr>';

    html += '<p><span class="comment_name">' + name +'：</span>' + content 
                    + '<br><span class="comment_time">' + time + '</span></p><a id="' + 
                    uuid + '" onClick="showCommentBox(\'' + uuid +'\');">评论</a>';

    for (var i = 0; i < replyList.length; i++) {
        reply = replyList[i]
        replyComment = getReplyComment(reply["name"], reply["content"], reply["time"]);
        html += replyComment;
    };

    html += '</article>';

    return html;
}

function getReplyComment (name, content, time) {
    var html = '<div class="comment_reply"><p><span class="comment_name">' + name + '：</span>' +
                        content + '<br><span class="comment_time">' + time + '</span></p></div>'
    return html;
}

function getCommentPages (pre, next) {
    var html = '<div class="comment_pagelist"><ul>'
    html += '<li><a href="#">«</a></li><li><a href="#">»</a></li>';
    html += '</ui></div>';
    return html;
}

function showCommentBox(commentId) {
    var target = document.getElementById(commentId);
    var parent = target.parentNode;
    var childs = parent.getElementsByTagName('div');
    var div = null;
    for(var i=0;i<childs.length;i++){
        if(childs[i].title == commentId)
              div = childs[i];
    }

    if (div) {
        parent.removeChild(div);
    } else{
        var html = '<textarea rows="6" type="text" placeholder="写下你的评论..."></textarea>';
        html += '<div><input type="text" name="nickname" placeholder="nickname"></div>';
        html += '<div><input type="text" name="email" placeholder="email"></div>';
        html += '<div><button class="btn btn-send" onClick="sendReplyComment(\'' + commentId + '\');">发送</button></div>';
        div = document.createElement("div");
        div.setAttribute("class","commentBox");
        div.title = commentId;
        div.innerHTML = html;
        // console.log(target);
        insertAfter(div, target);
    };

}

//@param newElement新创建的元素
//@param targetElement传递的已知元素
function insertAfter(newElement, targetElement) {
    var parent = targetElement.parentNode;
    var divParent = targetElement.parentNode;//获取该div的父节点
    var newNode = newElement;//创建文本节点
    var next = targetElement.nextSibling;//获取div的下一个兄弟节点
    //判断兄弟节点是否存在
    if(next) {
        //存在则将新节点插入到div的下一个兄弟节点之前，即div之后
        divParent.insertBefore(newNode, next);
    } else {
        //不存在则直接添加到最后,appendChild默认添加到divParent的最后
        divParent.appendChild(newNode);
    }
}

function sendComment () {
    var target = document.getElementById("globeCommentBox");
    var textarea = target.getElementsByTagName("textarea");
    var input = target.getElementsByTagName("input");
    var content = textarea[0].value;
    var nickname = input[0].value;
    var email = input[1].value;
    console.log(content, nickname, email);
}

function sendReplyComment (commentId) {
    var target = document.getElementById(commentId).parentNode;
    var childs = target.getElementsByTagName("div");
    var div = null;
    for(var i=0;i<childs.length;i++){
        if(childs[i].title == commentId)
            div = childs[i];
    }
    
    var textarea = div.getElementsByTagName("textarea");
    var input = div.getElementsByTagName("input");
    var content = textarea[0].value;
    var nickname = input[0].value;
    var email = input[1].value;
    console.log(content, nickname, email);
    showCommentBox(commentId);
}




