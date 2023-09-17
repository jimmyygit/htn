<script lang="ts">
	import '../app.css';
	import ImagePath from '$lib/components/logo.png';
	import TopAppBar, { Row, Section, Title } from '@smui/top-app-bar';
	import IconButton from '@smui/icon-button';

	let imagePath = '$lib/components/logo.png';
	let prominent = false;
	let dense = false;
</script>

<div class="h-full flex flex-col">
	<div class="py-2 w-full flex items-center justify-center">
		<img src={ImagePath} alt="Logo" style="height: 50px" />
	</div>

	<div class="flex-1">
		<slot />
	</div>
</div>
