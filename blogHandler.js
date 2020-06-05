new Vue({
  el: '#blogHandler',
  data: {
    posts: ''
  },
  methods: {

  },
  mounted: {
    fetch('localhost:8000/posts')
      .then(jsonData => (this.posts = jsonData.message))
  }
});
new Vue({
  el: '#blogList',
  data: {
    posts: ''
  },
  methods: {
    
  },
  mounted: {
    fetch('localhost:8000/posts')
      .then(jsonData => (this.posts = jsonData.message))
  }
});
