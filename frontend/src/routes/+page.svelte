<script lang="ts">
	import Fab, { Icon } from '@smui/fab';
	import Tab, { Label } from '@smui/tab';
	import TabBar from '@smui/tab-bar';
	import Accordion, { Panel, Header, Content } from '@smui-extra/accordion';
	import IconButton from '@smui/icon-button';

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

  import List, { Item, Separator, Text } from '@smui/list';
 

</script>

<div class="relative h-full">
	<div>
		<TabBar tabs={['Tasks', 'Goals', 'Notes']} let:tab bind:active>
			<Tab {tab}>
				<Label>{tab}</Label>
			</Tab>
		</TabBar>
	</div>
	<br />
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
            <List class="demo-list">
              <Separator />
              {#each shoppingContent as shop}
                <Item on:SMUI:action={() => window.location.href = '/route1'}><Text>{shop}</Text></Item>
                <Separator />
              {/each}
            </List>
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
						<List class="demo-list">
              <Separator />
              {#each homeworkContent as homework}
                <Item on:SMUI:action={() => window.location.href = '/route1'}><Text>{homework}</Text></Item>
                <Separator />
              {/each}
            </List>
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
						<List class="demo-list">
              <Separator />
              {#each generalContent as general}
                <Item on:SMUI:action={() => window.location.href = '/route1'}><Text>{general}</Text></Item>
                <Separator />
              {/each}
            </List>
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
						<List class="demo-list">
              <Separator />
              {#each personalContent as personal}
                <Item on:SMUI:action={() => window.location.href = '/route1'}><Text>{personal}</Text></Item>
                <Separator />
              {/each}
            </List>
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
						<List class="demo-list">
              <Separator />
              {#each careerContent as career}
                <Item on:SMUI:action={() => window.location.href = '/route1'}><Text>{career}</Text></Item>
                <Separator />
              {/each}
            </List>
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
						<List class="demo-list">
              <Separator />
              {#each ideasContent as ideas}
                <Item on:SMUI:action={() => window.location.href = '/route1'}><Text>{ideas}</Text></Item>
                <Separator />
              {/each}
            </List>
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
						<List class="demo-list">
              <Separator />
              {#each forLaterContent as forLater}
                <Item on:SMUI:action={() => window.location.href = '/route1'}><Text>{forLater}</Text></Item>
                <Separator />
              {/each}
            </List>
					</Content>
				</Panel>
			{/if}
		</Accordion>
	</div>

	<Fab
		on:click={() => console.log('create item')}
		class="flex absolute left-1/2 -translate-x-1/2 bottom-4"
		color="primary"
	>
		<Icon class="material-icons">add</Icon>
	</Fab>
</div>
