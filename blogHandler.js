var blogHandler = new Vue({
  el: '#blogHandler',
  data: {
      posts: ''
  },
  mounted () {
    fetch('http://localhost:8000/posts')
      .then(response => response.json())
      .then(data => (this.posts = data.posts))
  }
});
var blogList = new Vue({
  el: '#blogList',
  data: {
      posts: ''
  },
  mounted () {
    fetch('http://localhost:8000/posts')
      .then(response => response.json())
      .then(data => (this.posts = data.posts))
  }
});
