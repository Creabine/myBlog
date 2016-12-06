var BlogList = new Vue({
	el:'#vueroot',
	data:{
		blogDetail:blogDetail,
		newComment:{
			name:'',
			email:'',
			content:''
		}
	},
	methods:{
		addnewComment:function(){
			this.$http({
				url:'newComment',
				method:'post'
			}).then(function(data){
				var jdata = data.body;
				this.blogDetail.comments.push(jdata);
			}, function(error){
				console.error(error);
			})
		}
	}
});