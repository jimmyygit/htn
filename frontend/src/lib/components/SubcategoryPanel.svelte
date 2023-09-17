<script lang="ts">
	import { Content, Header, Panel } from '@smui-extra/accordion';
	import IconButton, { Icon } from '@smui/icon-button';

	export let label: string;
	export let open: bool = false;
	export let content: any[] = [];
</script>

<Panel bind:open variant="unelevated">
	<Header>
		{label}
		<IconButton slot="icon" toggle pressed={open}>
			<Icon class="material-icons" on>expand_less</Icon>
			<Icon class="material-icons">expand_more</Icon>
		</IconButton>
	</Header>
	<Content>
		<ul>
			{#each content as item}
				<li>{item}</li>
			{/each}
		</ul>
	</Content>
</Panel>
