
<br>
<script lang="ts">
    import Button from '@smui/button'
    import Textfield from '@smui/textfield';
    
    
  
    let valueA = '';
</script>


<div class="columns margins">
    <div>
      <Textfield
        style="width: 500px"
        class="shaped-filled"
        variant="filled"
        bind:value={valueA}
        label="Note"
      >
      </Textfield>

      <Button on:click={() => alert(valueA)} color = "primary"> Add Note </Button>

    </div>
    
  </div>
  
  
  
  <style>
    * :global(.shaped-filled) {
      border-radius: 16px 16px 0 0;
    }
  </style>
  