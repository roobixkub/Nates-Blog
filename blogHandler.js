const defaultPost = [{
  title: 'Welcome to my blog!',
  content: "This is some default text that will display when the API is not running",
  img: 'https://placeimg.com/600/200/tech'
}]

var blogHandler = new Vue({
  el: '#blogHandler',
  data: {
      posts: defaultPost,
      bioImg: 'https://placeimg.com/150/100/people/grayscale'
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
      posts: defaultPost
  },
  mounted () {
    fetch('http://localhost:8000/posts')
      .then(response => response.json())
      .then(data => (this.posts = data.posts))
  }
});
