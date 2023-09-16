<script lang="ts">
	import ImagePath from '$lib/components/logo.png'
	import TopAppBar, { Row, Section, Title } from '@smui/top-app-bar';
	import IconButton from '@smui/icon-button';
	
	let imagePath = "$lib/components/logo.png"
	let prominent = false;
	let dense = false;
	let secondaryColor = false;
	
</script>

  
  <div class="flexy">
	
	  <TopAppBar
		variant="static"
		{prominent}
		{dense}
		color={secondaryColor ? 'secondary' : 'primary'}
	  >
		<Row>
		  <Section style="align-itmes: center; justify-content: center; display: flex">
			<img src={ImagePath} alt="Logo" style="height: 50px" >
			
		  </Section>
		</Row>
	  </TopAppBar>
	
	  
	</div>
  
  
  

  
  <style>
	
  
	.flexy {
	  display: flex;
	  flex-wrap: wrap;
	}
  
	
  </style>
  
<slot />
