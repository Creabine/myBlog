var BlogList = new Vue({
	el:'#vueroot',
	data:{
		BlogList:BlogList.blogList,
		isMoreBlog:true
	},
	methods:{
		getMoreBlogs:function(){
			console.log('getmore');
			this.$http({
		    		url:"moreblogs",
		    		method:"get"
		    }).then(function(data){
		    	var jdata = data.body;
				if( jdata.blogList.length > 0 ){
					//将取到的blogs放入显示
					this.BlogList = this.BlogList.concat(jdata.blogList);
				}else{
					this.isMoreBlog = false;
				}

		    },function(error){
		    	console.error(error);
		    });
		},
	}
});