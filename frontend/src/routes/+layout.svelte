<script lang="ts">
	import '../app.css';
	import ImagePath from '$lib/components/logo.png';
</script>

<div class="h-full flex flex-col">
	<div class="py-2 w-full flex items-center justify-center">
		<img src={ImagePath} alt="Logo" style="height: 50px" />
	</div>

	<div class="flex-1">
		<slot />
	</div>
</div>
