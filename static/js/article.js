/*
 * JS related to article.{html,css} for managing functions inside blog posts
 */

// Expand/Contract atricle body when clicking article-expand button
document.querySelector('#articles').addEventListener('pointerdown', function(e) {
  if (hasClass(e.target ,'article-expand')) {
    // Toggle article bottom padding
    var article = document.getElementById(e.target.id);
    article.classList.toggle('closed');

    // Toggle article post
    var article_body = article.querySelector('.article-body');
    article_body.classList.toggle('collapsed');

    // Toggle article summary
    var article_oneliner = article.querySelector('.article-oneliner');
    article_oneliner.classList.toggle('collapsed');

    // Toggle expand/contract icon
    e.target.icon == 'unfold-less' ? e.target.icon = 'unfold-more' : e.target.icon = 'unfold-less';
  }
});

