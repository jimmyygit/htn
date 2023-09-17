<script lang="ts">
	import Tab, { Label } from '@smui/tab';
	import TabBar from '@smui/tab-bar';
	import Accordion, { Panel, Header, Content } from '@smui-extra/accordion';
	import IconButton, { Icon } from '@smui/icon-button';
	import Button from '@smui/button';
	import { Input } from '@smui/textfield';

	let panel1Open = false;
	let panel2Open = false;
	let panel3Open = false;
	let active = 'Tasks';

	let shoppingContent = ['Test 1', 'test 2'];
	let homeworkContent = ['Test 3', 'test 4'];
	let generalContent = ['Test 5', 'test 6'];
	let personalContent = ['Test 7', 'test 8'];
	let careerContent = ['Test 9', 'test 10'];
	let ideasContent = ['Test 11', 'test 12'];
	let forLaterContent = ['Test 13', 'test 14'];

	let note = '';
	function submitNote() {}
</script>

<div class="flex flex-col relative h-full">
	<div class="drop-shadow-md mb-2">
		<div class="bg-white py-2 w-full flex items-center justify-center">
			<img src="/logo.png" alt="Logo" style="height: 50px" />
		</div>
		<TabBar class="bg-white" tabs={['Tasks', 'Goals', 'Notes']} let:tab bind:active>
			<Tab {tab}>
				<Label>{tab}</Label>
			</Tab>
		</TabBar>
	</div>
	<div class="accordion-container">
		<Accordion>
			{#if active === 'Tasks'}
				<Panel bind:open={panel1Open}>
					<Header>
						Shopping
						<IconButton slot="icon" toggle pressed={panel1Open}>
							<Icon class="material-icons" on>expand_less</Icon>
							<Icon class="material-icons">expand_more</Icon>
						</IconButton>
					</Header>
					<Content>
						<ul>
							{#each shoppingContent as shop}
								<li>{shop}</li>
							{/each}
						</ul>
					</Content>
				</Panel>
				<Panel bind:open={panel2Open}>
					<Header>
						Homework
						<IconButton slot="icon" toggle pressed={panel2Open}>
							<Icon class="material-icons" on>expand_less</Icon>
							<Icon class="material-icons">expand_more</Icon>
						</IconButton>
					</Header>
					<Content>
						<ul>
							{#each homeworkContent as homework}
								<li>{homework}</li>
							{/each}
						</ul>
					</Content>
				</Panel>
				<Panel bind:open={panel3Open}>
					<Header>
						General
						<IconButton slot="icon" toggle pressed={panel3Open}>
							<Icon class="material-icons" on>expand_less</Icon>
							<Icon class="material-icons">expand_more</Icon>
						</IconButton>
					</Header>
					<Content>
						<ul>
							{#each generalContent as general}
								<li>{general}</li>
							{/each}
						</ul>
					</Content>
				</Panel>
			{/if}
			{#if active === 'Goals'}
				<Panel bind:open={panel1Open}>
					<Header>
						Personal
						<IconButton slot="icon" toggle pressed={panel1Open}>
							<Icon class="material-icons" on>expand_less</Icon>
							<Icon class="material-icons">expand_more</Icon>
						</IconButton>
					</Header>
					<Content>
						<ul>
							{#each personalContent as personal}
								<li>{personal}</li>
							{/each}
						</ul>
					</Content>
				</Panel>
				<Panel bind:open={panel2Open}>
					<Header>
						Career
						<IconButton slot="icon" toggle pressed={panel2Open}>
							<Icon class="material-icons" on>expand_less</Icon>
							<Icon class="material-icons">expand_more</Icon>
						</IconButton>
					</Header>
					<Content>
						<ul>
							{#each careerContent as career}
								<li>{career}</li>
							{/each}
						</ul>
					</Content>
				</Panel>
			{/if}
			{#if active === 'Notes'}
				<Panel bind:open={panel1Open}>
					<Header>
						Ideas
						<IconButton slot="icon" toggle pressed={panel1Open}>
							<Icon class="material-icons" on>expand_less</Icon>
							<Icon class="material-icons">expand_more</Icon>
						</IconButton>
					</Header>
					<Content>
						<ul>
							{#each ideasContent as ideas}
								<li>{ideas}</li>
							{/each}
						</ul>
					</Content>
				</Panel>
				<Panel bind:open={panel2Open}>
					<Header>
						For Later
						<IconButton slot="icon" toggle pressed={panel2Open}>
							<Icon class="material-icons" on>expand_less</Icon>
							<Icon class="material-icons">expand_more</Icon>
						</IconButton>
					</Header>
					<Content>
						<ul>
							{#each forLaterContent as forLater}
								<li>{forLater}</li>
							{/each}
						</ul>
					</Content>
				</Panel>
			{/if}
		</Accordion>
	</div>

	<div class="flex-1" />

	<div class="p-4 flex items-baseline gap-2 bg-gray-100">
		<Input bind:value={note} class="solo-input" placeholder="Jot something down..." autofocus />
		<Button disabled={note.length === 0} on:click={submitNote}>Submit</Button>
	</div>
</div>

<style>
	* :global(.solo-input::placeholder) {
		color: var(--mdc-theme-on-surface, #000);
		opacity: 0.6;
	}
</style>
