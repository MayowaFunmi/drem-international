var showTime = function() {
    var disp = document.getElementById('clock');
    var meridian = "AM"
    var myDate = new Date();
    var hour = myDate.getHours();
    var minute = myDate.getMinutes();
    var second = myDate.getSeconds();

    if (hour > 11) {
        meridian = "PM"
    }

    if (hour >= 12) {
        hour = hour - 12
    };

    if (minute < 10) {
        minute = "0" + minute
    };

    if (second < 10) {
        second = "0" + second
    };

    currentTime = hour + ":" + minute + ":" + second + meridian;
    disp.innerHTML = currentTime;

};
showTime();
setInterval(showTime, 1000);

/*
    Social Share links:

    Whatsapp:
    https://api.whatsapp.com/send?text=[post-title] [post-url]

    Facebook:
    https://www.facebook.com/sharer.php?u=[post-url]

    Twitter:
    https://twitter.com/share?url=[post-url]&text=[post-title]&via=[via]&hashtags=[hashtags]

    Email:
    $email = 'mailto:?subject=' . $[post-title] . '&body=Check out this site: '. $[post-url] .'" title="Share by Email';

    LinkedIn
    https://www.linkedin.com/shareArticle?url=[post-url]&title=[post-title]

    Telegram
    https://t.me/share/url?url={url}&text={text}

*/
const facebookBtn = document.querySelector('.facebook-btn')
const twitterBtn = document.querySelector('.twitter-btn')
const whatsappBtn = document.querySelector('.whatsapp-btn')
const linkedinBtn = document.querySelector('.linkedin-btn')
const telegramBtn = document.querySelector('.telegram-btn')

function init() {
    let postUrl = encodeURI(document.location.href)
    let postTitle = encodeURI('Read the latest post from DREM international: ')

    facebookBtn.setAttribute('href', `https://www.facebook.com/sharer.php?u=${postUrl}`)
    twitterBtn.setAttribute('href', `https://twitter.com/share?url=${postUrl}&text=${postTitle}`)
    whatsappBtn.setAttribute('href', `https://api.whatsapp.com/send?text=${postTitle} ${postUrl}`)
    linkedinBtn.setAttribute('href', `https://www.linkedin.com/shareArticle?url=${postUrl}&title=${postTitle}`)
    telegramBtn.setAttribute('href', `https://t.me/share/url?url=${postUrl}&text=${postTitle}`)
}

init()