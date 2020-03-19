<template>
  <div class="container" v-if="articles && articles.length">
    <div class="row" v-for="article in articles" v-bind:key="article.id">
      <div class="col-md-12">
        <h1>{{ article.heading }}</h1>
        <p>{{ article.body }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Articles',
  data () {
    return {
      articles: []
    }
  },
  created () {
    this.fetchArticles()
    this.timer = setInterval(this.fetchArticles, 3000)
  },
  methods: {
    fetchArticles () {
      this
        .$http.get('http://127.0.0.1:8000/articles/')
        .then(response => {
          console.log(response.data)
          this.articles = response.data
        })
    },
    cancelAutoUpdate () { clearInterval(this.timer) }

  },
  beforeDestroy () {
    clearInterval(this.timer)
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
