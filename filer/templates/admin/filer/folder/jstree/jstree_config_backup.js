var get_default_options = function() {
	var bla = { //jQuery.tree.defaults
		plugins : {
			hotkeys: {}
			//contextmenu: {}
		},
		data: { 
			type : "json",
			async : true,
			opts : {
				method : "GET",
				url : "/admin/filer/folder/api/folder/"
			}
		},
		callback: { 
			onmove: function(node, ref_node, type, tree_obj, rb){
				//alert("moving '" + tree_obj.get_text(node) + "' (" + rb + ") to '" + tree_obj.get_text(ref_node)+"'");
				$.ajax({
					type:'POST',
					dataType: 'json',
					url: '{% url admin:filer-directory_browser-move %}',
					data: { 'src_objtype': tree_obj.get_type(node), 
							'src_id': tree_obj.get_node(node).attr('id'),
							'ref_objtype': tree_obj.get_type(ref_node),
							'ref_id': tree_obj.get_node(ref_node).attr('id'),
							'ref_type': type
					},
					async: true,
					success: function(data, textStatus, request) {
						//alert('success: ' + textStatus + '   ' + data);
					},
					error: function(request, textStatus, errorThrown) {
						//alert('failed: ' + textStatus + '    ' + errorThrown);
						$.tree.rollback(rb);
					}
				}
				);
			},
			onrename: function(node, tree_obj, rb){
				//alert("renaming '" + tree_obj.get_text(node) + "' (" + rb + ") to '" + tree_obj.get_text(ref_node)+"'");
				$.ajax({
					type:'POST',
					dataType: 'json',
					url: '{% url admin:filer-directory_browser-rename %}',
					data: { 'obj_type': tree_obj.get_type(node), 
							'obj_id': tree_obj.get_node(node).attr('id'),
							'obj_new_name': tree_obj.get_text(node)
					},
					async: true,
					success: function(data, textStatus, request) {
						//alert('success: ' + textStatus + '   ' + data);
					},
					error: function(request, textStatus, errorThrown) {
						//alert('failed: ' + textStatus + '    ' + errorThrown);
						$.tree.rollback(rb);
					}
				}
				);
			},
			oncreate: function(node, ref_node, type, tree_obj, rb){
				console.log(node);
				$.ajax({
					type:'POST',
					dataType: 'json',
					url: '{% url admin:filer-directory_browser-create %}',
					data: { 'node_type': tree_obj.get_type(node),
							'node_name':tree_obj.get_text(node), 
							'ref_node_id': tree_obj.get_node(ref_node).attr('id'),
							'ref_node_type': tree_obj.get_type(ref_node),
							'ref_node_rel': type
					},
					async: true,
					success: function(data, textStatus, request) {
						//alert('success: ' + textStatus + '   ' + data);
					},
					error: function(request, textStatus, errorThrown) {
						//alert('failed: ' + textStatus + '    ' + errorThrown);
						$.tree.rollback(rb);
					}
				}
				);
			},
			ondata: function(data, tree_obj) {
				//console.log(data);
				/*
				var r = new Array();
				$.each(
					data,
					function( i, v ){
						x = {"attributes":{"id":v.id,"rel":v.type},"data":{"title":v.name}}
						if (v.item_count>0) {
							x.state = "closed";
						};
						r[i] = x;
					}
				);
				return r
				*/
				return data;
			}
		},
		rules :{
		},
		types: {
			"default": {
				deletable: false,
				renameable: false
			},
			"category": {
				draggable: false,
				deletable: false,
				valid_children: ["folder"]
			},
			"category_item": {
				
			},
			"folder": {
				valid_children: ["file","folder"],
				renameable: true
			},
			"file": {
				valid_children: "none",
				max_children: 0,
				max_depth: 0,
				icon: {
					image: "/media/filer/icons/file_16x16.png"
				},
				renameable: true
			}
		},
		ui: {
			theme_name : "apple",
			dots: false
		}
	};
	return bla;
};